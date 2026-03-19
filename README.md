# five-in-a-row

A single-file Gomoku front end with a cyberpunk-style UI, responsive layout, and lightweight AI opponent.

[English](./README.md) | [简体中文](./README.zh-CN.md)

## Overview

This project is a static browser game built around one main file: [`index.html`](./index.html). It is designed to be easy to run, easy to deploy, and easy to modify.

The current version focuses on:

- a bold single-page interface
- click and touch-based play on desktop and mobile
- a simple AI that opens at the center and answers with threat scanning plus lightweight alpha-beta search
- local best-time storage with `localStorage`
- zero build tooling and zero runtime dependencies

## Current Gameplay

- The AI plays white and always opens first.
- The player plays black.
- Click or tap an empty intersection to place a stone.
- Five in a row wins horizontally, vertically, or diagonally.
- The status panel, turn panel, move count, latency, and mission feed update during play.

## Features

- Single-file app: all markup, styles, and game logic live in `index.html`
- Responsive layout: tuned for desktop, tablet, and phone screens
- Touch support: mobile tap interaction is handled directly on the canvas
- Live UI state: system status, turn state, move count, timer, and message log
- Persistent record: best win time is saved in the browser
- Easy hosting: works well as a static page on GitHub Pages or any static host

## Run Locally

You can open the HTML file directly, but a local server is the safer option for browser testing.

### Option 1: Open the file directly

Open [`index.html`](./index.html) in your browser.

### Option 2: Use a local server

```bash
cd five-in-a-row
python3 -m http.server 8080
```

Then visit:

```text
http://localhost:8080
```

## Mobile Testing

To verify the phone layout and touch interaction:

1. Start the local server.
2. Open the page in your browser.
3. Use responsive mode in DevTools, or open it on a real phone on the same network.
4. Check these points:
   - the page does not overflow horizontally
   - the board scales to the available width
   - tapping intersections places stones correctly
   - buttons and panels remain readable on small screens

## Project Structure

```text
five-in-a-row/
├── index.html
├── README.md
├── README.zh-CN.md
├── DEPLOY.md
├── PAGES_GUIDE.md
├── PR_GUIDE.md
└── SIMPLE_DEPLOY.md
```

## Implementation Notes

- Rendering uses HTML5 Canvas.
- The UI is built with plain HTML and CSS.
- The game logic is written in vanilla JavaScript.
- The current AI is heuristic-based and intentionally lightweight.

This is not a tournament-grade engine. It is a front-end-focused Gomoku project with a presentable interface and playable local opponent.

## Deployment

Because the project is static, you can deploy it to:

- GitHub Pages
- Netlify
- Vercel static hosting
- any basic file server

Repository deployment notes are available in:

- [`DEPLOY.md`](./DEPLOY.md)
- [`PAGES_GUIDE.md`](./PAGES_GUIDE.md)
- [`SIMPLE_DEPLOY.md`](./SIMPLE_DEPLOY.md)

## Contributing

If you want to improve the UI, AI, or gameplay behavior, start with [`index.html`](./index.html). Contribution notes are in [`PR_GUIDE.md`](./PR_GUIDE.md).

## Status

The repository is currently oriented around a polished static front end. If you extend it further, keep the README aligned with the real implementation instead of aspirational features.
