<div align="center">
  <img src="./banner.svg" alt="host-recon" width="800">
</div>

# host-recon

> Local host situational-awareness scaffold

This repository currently contains a CLI scaffold, not a host-enumeration
implementation. It prints the supplied target identifier and a status message;
it does not inspect the local host, resolve or contact a target, or perform
network activity.

## Install

```bash
git clone https://github.com/amooryx/host-recon.git
cd host-recon
```

## Usage

```bash
python host_recon.py <target>
```

| Flag | Description |
|---|---|
| `-o, --output` | Write results to a file |
| `-v, --verbose` | Verbose output |
| `-y, --yes` | Skip the authorisation prompt |

By default, the report is printed to standard output. `-o/--output` writes the
report to a new UTF-8 text file; it refuses to overwrite an existing path and
returns an error if the file cannot be created. No target activity occurs in
either mode.

## Disclaimer

> **Authorised security testing only.** Use this against systems you own or have
> explicit written permission to test. The CLI prompts for authorisation unless
> `-y` is supplied. This scaffold performs no testing or target interaction.

## Author

**Omar Khalid** — [omareldemery.com](https://omareldemery.com) | [@amooryx](https://github.com/amooryx)

Certifications: OSCP+ · OSCP · CRTP · eWPTX · eCPPT · eCDFP · eCIR · eJPT
