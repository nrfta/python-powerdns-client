# python-netbox-client

This is the `codegen` branch of the project. It is only used to configure and trigger code generation to `master`.

## Instructions

You can control the `config.json` and `.github/workflows` from here. When NetBox updates their API, download the swagger
and save as `netbox_swagger.json`.

When this branch is pushed to GitHub, the `codegen.yaml` workflow will be triggered.

```
git push origin codegen
```

The workflow will commit the newly generated code to `master`.

This `codegen` branch should never be merged to `master`. Its only purpose is to configure the code generator and run the workflow.