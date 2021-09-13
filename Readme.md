## Give Me Some Ports!
A simple script to allocate a free port at request time.  The script binds to port 0 (kernel), the kernel then will allocate a free port from its IP ports pool.

## Why this script?
Mainly to save time and frustration searching for available ports on a machine. This is especially handy when working with containers or any application that require port binding.

## Usage
- `chmod +x givemeport.py`
- Add the script to `$PATH` 
- Run: `$ givemeport`

Tested on: CentOS 8, Ubuntu 20.04, Fedora 34,33
