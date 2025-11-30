# autohotkey-demo
A small demo showing how AutoHotkey improved my workflow—and honestly, changed my life a bit for the better.

### context:
I first used AutoHotkey by modifying a feature created by my senior at work.
That small improvement unexpectedly made my workflow faster, earned trust from my colleagues, and opened my eyes to how powerful automation can be.
This repo is a simple demonstration of that idea.

## input-trigger-demo-ahk.ahk
This script lets you save any sequence of inputs and trigger them with one single hotkey.
Think of it like creating your own custom macro:

Press one key → AutoHotkey runs multiple actions for you.

### How it works
1. You choose the action or text you want to automate.
2. You assign it to a single hotkey.
3. When that hotkey is pressed, AutoHotkey sends all the inputs automatically—just like a gaming macro, but for real productivity.

## time-trigger-demo.ahk
This script lets you save any sequence of inputs and trigger them either at a specific time you set or at a repeated interval.

### How it works
1. You choose the action or text you want to automate.
2. You decide whether it should run at a specific time or at a repeating interval.
3. When the scheduled time is reached, AutoHotkey sends all the inputs automatically—just like a gaming macro, but for real productivity.

## input-runapps-demo.ahk

This script demonstrates how AutoHotkey can launch applications instantly using a single hotkey.
Instead of searching, clicking, or navigating menus, you can bind any app to a shortcut and open it the moment you need it.

### How it works
1. You choose an application you often open (browser, notes app, IDE, anything).
2. You assign a hotkey (e.g., Ctrl + Q, Alt + S, etc.).
3. Whenever the hotkey is pressed, AutoHotkey launches the app immediately.
It’s a tiny improvement, but it eliminates small delays that add up over a full workday.

## time-runapps-demo.ahk
This script expands on the previous idea by letting AutoHotkey run an application automatically based on time, without pressing anything.
It’s useful for scheduled tasks—like opening your stock screener every morning, running a report, or preparing a tool before a meeting.

### How it works
1. You specify the application you want to run.
2. You set a specific time or a repeated interval (e.g., every hour).
3. When the trigger time arrives, AutoHotkey launches the app in the background.
This is the foundation for building fully automated workflows—apps that prepare themselves before you even sit down.
