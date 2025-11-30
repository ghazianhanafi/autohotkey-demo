#SingleInstance Force
#Persistent   ; <-- THIS is what was missing

; ====== CONFIG ======
PythonExe := "C:\Users\ghazi\AppData\Local\Programs\Python\Python313\pythonw.exe"
PythonScript := "C:\Users\ghazi\OneDrive\Bismillah Intellectual Property of Ghazian Hirzi Hanafi\SCI035_RESEARCH\08_Portofolio\10_AHK\adzan_next.py"
; ====================

; Run every 10 seconds
SetTimer, CheckAdzan, 10000
return


CheckAdzan:
    FullCmd := """" . PythonExe . """ """ . PythonScript . """"
    result := RunWaitGet(FullCmd)

    If (result = "")
    {
        TrayTip, ERROR, Python returned empty output., 5, 3
        return
    }

    StringSplit, parts, result, |
    mins := parts1
    secs := parts2

    TrayTip, Adzan Reminder, % "Time left: " mins " minutes (" secs " sec)", 5, 1
return


RunWaitGet(command) {
    shell := ComObjCreate("WScript.Shell")
    exec := shell.Exec(command)
    return exec.StdOut.ReadAll()
}
