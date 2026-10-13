# protos

Shared Protocol Buffer definitions for sdkim96 services, managed as a single
[buf](https://buf.build) module.

## Layout

```
buf.yaml, buf.lock       buf module config and dependency lockfile
buf.gen.yaml             codegen config (Go + Python)
identity/v1/             identity.v1 package: Account
knowledge/v1/            knowledge.v1 package: Workspace, Member, File, FileUrl, Source
knowledge/README.md      notes specific to the knowledge package
gen/go/                  generated Go code, committed (module github.com/sdkim96/protos)
gen/python/              generated Python code, committed (installable package sdkim96-protos)
```

Every resource message carries a `google.api.resource` option and
`google.api.field_behavior` annotations (`REQUIRED` / `OUTPUT_ONLY` /
`OPTIONAL` / `IDENTIFIER`). Cross-resource references use
`google.api.resource_reference`. Resource types are namespaced per package:
`identity.api.sdkim96.com/*` and `knowledge.api.sdkim96.com/*`.

## Consuming this module

### Go

```sh
go get github.com/sdkim96/protos@v0.1.0
```

```go
import identityv1 "github.com/sdkim96/protos/gen/go/identity/v1"
import knowledgev1 "github.com/sdkim96/protos/gen/go/knowledge/v1"
```

### Python

Install directly from the git subdirectory that holds the generated package:

```sh
pip install "git+https://github.com/sdkim96/protos.git@v0.1.0#subdirectory=gen/python"
```

```python
from identity.v1 import account_pb2
from knowledge.v1 import file_url_pb2
```

### Raw `.proto` files

To compile these definitions yourself (e.g. with your own `buf.gen.yaml`),
add this repo as a buf module dependency, or clone it at a tag and point your
`buf.yaml` `deps`/include paths at the checkout. The module root is the repo
root, so import paths are module-relative, e.g.
`import "knowledge/v1/file_url.proto";`.

## Versioning policy

- Tags are semver (`v0.1.0`, `v0.2.0`, ...) on `main`.
- Field numbers are never reused or renumbered once a tag ships. Renaming a
  field, message, or package is a breaking wire-format change only if the
  field *number* or *type* changes — pure renames are fine pre-1.0 but should
  stop once a real consumer depends on the generated code.
- `v1` packages (`identity.v1`, `knowledge.v1`) are considered **unstable**
  until a consumer takes a dependency on a tagged release. Up to that point,
  breaking changes may ship without a major version bump. After that point,
  breaking changes require a new major-versioned package
  (`knowledge.v2`, ...) rather than breaking `v1` in place.
- `buf breaking --against '.git#branch=main'` runs in CI on every PR and
  should be treated as a hard gate once this module has real consumers.

## Development

```sh
make lint       # buf lint
make format     # buf format -w .
make breaking   # buf breaking --against '.git#branch=main'
make generate   # buf generate (writes gen/go, gen/python)
make check      # generate + build + format -d --exit-code + lint + breaking + drift check
```

Run `make check` before opening a PR — it's the same thing CI runs.
