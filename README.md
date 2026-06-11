# MORAI ROS2 Messages

This package contains the ROS 2 message and service definitions (`.msg`, `.srv`) required for interfacing with **MORAI SIM: Drive**, an autonomous driving simulator.

## Resources

- [Website](https://www.morai.ai/)
- **Documentation**:
  - [MORAI ROS2 Messages](https://morai-autonomous.github.io/MORAI-ROS2_morai_msgs/)
  - [MORAI SIM Manual (English)](https://morai-sim-drive-user-manual-en-24-r2.scrollhelp.site/morai-sim-drive-user-manual-en-24.r2/Working-version/?l=en)
  - [MORAI SIM Manual (Korean)](https://help-morai-sim.scrollhelp.site/)
- **Quickstart Guides**:
  - [ROS2 Environment Setup](https://morai-sim-drive-user-manual-en-24-r2.scrollhelp.site/morai-sim-drive-user-manual-en-24.r2/Working-version/developer-setup-for-ros2)
  - [Data Sync Example](https://morai-sim-drive-user-manual-en-24-r2.scrollhelp.site/morai-sim-drive-user-manual-en-24.r2/Working-version/ros2-data-sync-example)

## Documentation

The message and service reference is generated from the `.msg`/`.srv` definitions and
published with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) +
[mike](https://github.com/jimporter/mike) (multi-version).

```bash
# Install the docs toolchain
pip install -r docs-requirements.txt

# Generate the per-message/service pages from the definitions
python docs/generate_docs.py

# Live preview
mkdocs serve
```

Versions are published to the `gh-pages` branch automatically by
[`.github/workflows/docs.yml`](.github/workflows/docs.yml):

- Pushes to `main`/`master` publish the in-progress docs as the **`dev`** version.
- Pushing a `v*` tag publishes that version and moves the **`latest`** alias (the default
  shown to visitors) to it.
- You can also publish a specific version manually via the **Run workflow** button
  (`workflow_dispatch`).

To publish a version locally instead of via CI:

```bash
mike deploy --push --update-aliases v1.2.0 latest
mike set-default --push latest
```

## License

This project is licensed under the [MIT License](LICENSE).
