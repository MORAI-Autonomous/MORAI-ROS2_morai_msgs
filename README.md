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
[`.github/workflows/docs.yml`](.github/workflows/docs.yml). Every version is built with the
tooling on `main`, overlaying each ref's `msg`/`srv` definitions
([`docs/build_version.sh`](docs/build_version.sh)), and the navigation/overview pages are
auto-generated to match whatever definition set is present:

- Pushes to `main`/`master` publish the in-progress docs as the **`dev`** version, which is
  the default shown to visitors at the site root.
- Pushing a release tag (`v*`, or `NN.RN` such as `26.R1`) publishes that release as its
  own selectable version. `dev` remains the default.
- Run the workflow manually with **Run workflow → backfill** checked to (re)build and
  publish every version at once (`dev` plus the release tags `24.R2` and `26.R1`).

To publish a version locally instead of via CI (overlays the ref's definitions, builds with
the current tooling, and pushes to `gh-pages`):

```bash
docs/build_version.sh main dev     # publish the dev version
docs/build_version.sh 26.R1 26.R1  # publish a release version
mike set-default --push dev         # point the site root at dev
```

## License

This project is licensed under the [MIT License](LICENSE).
