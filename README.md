# MAISHacks

Genetic Dungeon automates D&D map-making. Give a text paragraph describing a desired dungeon: LLM parses theme/size, BSP creates dungeon layout, a genetic algorithm populates objects, and outputs PNG.

MAIS Hacks Hackathon on November 1st and 2nd, 2025. Contributors include @puganinithepug, @mattiagreiche, @GawainsGreenGirdle

## Inspiration
We were inspired by how tedious it can be for Dungeon Masters to design detailed D&D maps that fit their adventures. We wanted to create a tool that could take a single descriptive paragraph and automatically generate a complete, themed dungeon.

## What it does
The Genetic Dungeon converts a short text prompt into a dungeon map. It uses an LLM to interpret the theme and size, binary space partitioning (BSP) to generate room layouts, a genetic algorithm to populate objects and decorations, and finally renders the result as a PNG.

## How we built it
We divided the project into a pipeline of four main stages: prompt interpretation, room generation, object placement, and image rendering. Drawing out the entire system architecture at the start was crucial. It gave us a clear sense of how data would flow between steps and helped us debug complex interactions later on. We built in Python and connected each module through structured data formats.

## Challenges we ran into
The hardest part was getting all components to communicate cleanly. Each stage produced different data outputs, so synchronizing formats and ensuring consistency across the pipeline took a lot of trial and error. Another major challenge was optimizing the genetic algorithm so that it produced maps that made intuitive sense.

## Accomplishments that we're proud of
We’re incredibly proud that we built a full end-to-end system that goes from natural language input to visual output, that works cohesively. It's quite cool to see a simple paragraph turn into a full dungeon image that could actually be used in a game.

## What we learned
We learned a lot about system design, procedural generation, and how to connect AI with traditional algorithms. We also learned how valuable clear planning and communication are in a group project.

## What's next for Genetic Dungeon Generation
We plan on increasing the LLM's role by prompting it to generate the desired objects and monsters (from a set of possibilities, depending on which PNG assets are available to us) that should be present in the dungeon, depending on the text input. This way, dungeons are much more unique and true to the original text input.

The images we used for this project are sourced from Two minute tabletop. Their licensing agreement can be found by following this link: https://2minutetabletop.com/faq/license-and-attribution/ .
