// Entry for make.fun's news-image-20261118 bounty (Node 22, stdlib only).
//
// The image is drawn by draw.py (Pillow) and committed here as entry.png;
// this program's only job is to place that image at the grader's output
// path. It creates the output directory when needed and refuses to run
// if the image is missing, so a failed build is loud instead of silent.
//
// Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

if (!existsSync(source)) {
  throw new Error(`entry.png not found next to main.ts (${source})`);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);
console.log(`wrote ${target}`);
