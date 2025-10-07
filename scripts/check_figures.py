#!/usr/bin/env python3
import sys
from pathlib import Path

VECTOR_FORMATS = {'.pdf', '.svg', '.eps'}
RASTER_FORMATS = {'.png', '.jpg', '.jpeg'}

def check_figures():
    figures_dir = Path('figures')
    
    if not figures_dir.exists():
        print("ℹ️  No figures directory")
        return 0
    
    warnings = []
    
    for fig in figures_dir.rglob('*'):
        if not fig.is_file():
            continue
        
        ext = fig.suffix.lower()
        
        if ext in RASTER_FORMATS:
            stem = fig.stem
            vector_exists = any(
                (figures_dir / f"{stem}{v}").exists()
                for v in VECTOR_FORMATS
            )
            
            if not vector_exists:
                warnings.append(f"::warning::{fig}: Raster format without vector alternative")
    
    if warnings:
        print("⚠️  Figure format warnings:")
        for w in warnings:
            print(f"  {w}")
        print("\n💡 Prefer vector formats (PDF, SVG, EPS)")
    else:
        print("✅ Figure formats OK")
    
    return 0

if __name__ == '__main__':
    sys.exit(check_figures())
