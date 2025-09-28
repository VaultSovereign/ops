#!/usr/bin/env python3
"""SSH automation helper for VaultMesh operations."""

import argparse
import os
import subprocess
import sys
from pathlib import Path


def run_cmd(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run command with error handling."""
    try:
        return subprocess.run(cmd, check=check, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"[ssh-auto] Command failed: {' '.join(cmd)}", file=sys.stderr)
        print(f"[ssh-auto] Error: {e.stderr}", file=sys.stderr)
        sys.exit(1)


def check_ssh_agent():
    """Ensure SSH agent is running and keys are loaded."""
    print("[ssh-auto] Checking SSH agent...")
    
    # Check if agent is running
    result = run_cmd(["ssh-add", "-l"], check=False)
    if result.returncode != 0:
        print("[ssh-auto] Starting SSH agent...")
        run_cmd(["ssh-add", "--apple-use-keychain"])
    
    # Load VaultMesh keys
    vaultmesh_key = Path.home() / ".ssh" / "vaultmesh_master"
    if vaultmesh_key.exists():
        print("[ssh-auto] Loading VaultMesh master key...")
        run_cmd(["ssh-add", "--apple-use-keychain", str(vaultmesh_key)])
    
    print("[ssh-auto] SSH agent ready")


def test_connections():
    """Test connections to configured hosts."""
    hosts = ["forge", "core-01", "ai-node", "brain"]
    
    print("[ssh-auto] Testing connections...")
    for host in hosts:
        print(f"[ssh-auto] Testing {host}...")
        result = run_cmd([
            "ssh", "-o", "ConnectTimeout=5", 
            "-o", "BatchMode=yes",
            host, "echo 'Connection OK'"
        ], check=False)
        
        if result.returncode == 0:
            print(f"[ssh-auto] ✓ {host}: {result.stdout.strip()}")
        else:
            print(f"[ssh-auto] ✗ {host}: Connection failed")


def setup_tunnels():
    """Set up SSH tunnels for VaultMesh access."""
    print("[ssh-auto] Setting up VaultMesh tunnels...")
    
    # Check if tunnel is already running
    result = run_cmd(["pgrep", "-f", "ssh.*vm-funnel"], check=False)
    if result.returncode == 0:
        print("[ssh-auto] VaultMesh tunnel already running")
        return
    
    print("[ssh-auto] Starting VaultMesh tunnel (vm-funnel)...")
    print("[ssh-auto] Local ports: 8800 → :3081, 8801 → :80")
    
    # Start tunnel in background
    subprocess.Popen([
        "ssh", "-N", "-f", "vm-funnel"
    ])
    
    print("[ssh-auto] Tunnel started. Access VaultMesh at:")
    print("[ssh-auto]   http://localhost:8800 (main)")
    print("[ssh-auto]   http://localhost:8801 (web)")


def show_status():
    """Show SSH connection status."""
    print("[ssh-auto] SSH Status Report")
    print("=" * 40)
    
    # SSH agent status
    result = run_cmd(["ssh-add", "-l"], check=False)
    if result.returncode == 0:
        print("SSH Agent: ✓ Running")
        print("Loaded keys:")
        for line in result.stdout.strip().split('\n'):
            if line:
                print(f"  - {line}")
    else:
        print("SSH Agent: ✗ Not running or no keys")
    
    print()
    
    # Active connections
    result = run_cmd(["ss", "-tn"], check=False)
    if result.returncode == 0:
        ssh_conns = [line for line in result.stdout.split('\n') if ':22' in line and 'ESTAB' in line]
        if ssh_conns:
            print("Active SSH connections:")
            for conn in ssh_conns:
                print(f"  - {conn}")
        else:
            print("Active SSH connections: None")
    
    print()
    
    # Tunnel status
    result = run_cmd(["pgrep", "-f", "ssh.*vm-funnel"], check=False)
    if result.returncode == 0:
        print("VaultMesh tunnel: ✓ Running")
        print("  - http://localhost:8800 → core-01:3081")
        print("  - http://localhost:8801 → core-01:80")
    else:
        print("VaultMesh tunnel: ✗ Not running")


def main():
    parser = argparse.ArgumentParser(description="SSH automation for VaultMesh")
    parser.add_argument("action", choices=[
        "agent", "test", "tunnel", "status", "all"
    ], help="Action to perform")
    
    args = parser.parse_args()
    
    if args.action == "agent":
        check_ssh_agent()
    elif args.action == "test":
        test_connections()
    elif args.action == "tunnel":
        setup_tunnels()
    elif args.action == "status":
        show_status()
    elif args.action == "all":
        check_ssh_agent()
        test_connections()
        setup_tunnels()
        show_status()


if __name__ == "__main__":
    main()
