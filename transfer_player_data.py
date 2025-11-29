#!/usr/bin/env python3
"""
Transfer player data from one player to another in Minecraft offline mode.
Transfers: inventory, levels, ender chest, health, food, and experience.
"""

import sys
import os
import copy
from nbtlib import File, Compound, List, String, Int, Float, Double, Byte, Short, Long

def transfer_player_data(source_uuid, target_uuid, playerdata_dir):
    """Transfer player data from source to target."""
    
    source_file = os.path.join(playerdata_dir, f"{source_uuid}.dat")
    target_file = os.path.join(playerdata_dir, f"{target_uuid}.dat")
    
    # Check if files exist
    if not os.path.exists(source_file):
        print(f"ERROR: Source playerdata file not found: {source_file}")
        return False
    
    if not os.path.exists(target_file):
        print(f"ERROR: Target playerdata file not found: {target_file}")
        return False
    
    # Backup target file
    backup_file = f"{target_file}.backup"
    print(f"Creating backup: {backup_file}")
    os.system(f"cp {target_file} {backup_file}")
    
    # Load both files
    print(f"Loading source file: {source_file}")
    source_nbt = File.load(source_file, gzipped=True)
    
    print(f"Loading target file: {target_file}")
    target_nbt = File.load(target_file, gzipped=True)
    
    # Fields to transfer
    fields_to_transfer = [
        'Inventory',           # Main inventory
        'EnderItems',         # Ender chest (correct field name)
        'XpLevel',            # Experience level
        'XpP',                # Experience progress (0.0-1.0)
        'XpTotal',            # Total experience
        'foodLevel',          # Food level
        'foodSaturationLevel', # Food saturation
        'foodExhaustionLevel', # Food exhaustion
        'Health',             # Health
        'AbsorptionAmount',   # Absorption hearts
    ]
    
    print("\nTransferring data:")
    transferred_count = 0
    
    for field in fields_to_transfer:
        if field in source_nbt:
            # Deep copy to preserve all item data including components/enchantments/trims
            # Using copy.deepcopy ensures all nested NBT structures are preserved
            target_nbt[field] = copy.deepcopy(source_nbt[field])
            print(f"  ✓ {field} (with all components/enchantments/trims)")
            transferred_count += 1
        else:
            print(f"  ✗ {field} (not found in source)")
    
    # Save the modified target file
    print(f"\nSaving modified target file: {target_file}")
    target_nbt.save(target_file, gzipped=True)
    
    print(f"\n✓ Transfer complete! Transferred {transferred_count} fields.")
    print(f"  Backup saved at: {backup_file}")
    return True

if __name__ == "__main__":
    # UUIDs
    STEELSHARK_UUID = "8813206a-3133-323c-aae2-4d9f757b0469"
    IDOVAI_UUID = "abb87e38-59fe-3a94-a04c-ceebd573fe56"
    
    playerdata_dir = "/home/ubuntu/minecraft-server/data/world/playerdata"
    
    print("=" * 70)
    print("MINECRAFT PLAYER DATA TRANSFER")
    print("=" * 70)
    print(f"Source: The_SteelShark ({STEELSHARK_UUID})")
    print(f"Target: IDovaI ({IDOVAI_UUID})")
    print("=" * 70)
    print()
    
    success = transfer_player_data(STEELSHARK_UUID, IDOVAI_UUID, playerdata_dir)
    
    if success:
        print("\n" + "=" * 70)
        print("SUCCESS! The_SteelShark's data has been transferred to IDovaI.")
        print("=" * 70)
        print("\n⚠️  IMPORTANT: Make sure the Minecraft server is stopped before")
        print("   making this change. Restart the server after the transfer.")
        sys.exit(0)
    else:
        print("\n" + "=" * 70)
        print("ERROR: Transfer failed!")
        print("=" * 70)
        sys.exit(1)

