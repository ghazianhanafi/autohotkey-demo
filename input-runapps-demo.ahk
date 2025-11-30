; ====== CONFIG ======
PythonExe := "C:\Users\ghazi\AppData\Local\Programs\Python\Python313\pythonw.exe"
PythonScript := "C:\Users\ghazi\OneDrive\Bismillah Intellectual Property of Ghazian Hirzi Hanafi\SCI035_RESEARCH\08_Portofolio\10_AHK\adzan_next.py"
; ====================

^q::
    FullCmd := """" PythonExe """ """ PythonScript """"
    result := RunWaitGet(FullCmd)

    StringSplit, parts, result, |
    mins := parts1
    secs := parts2

    MsgBox, 64, Adzan Reminder, Time left until next adzan:`n%mins% minutes 
return


RunWaitGet(command) {
    shell := ComObjCreate("WScript.Shell")
    exec := shell.Exec(command)
    return exec.StdOut.ReadAll()
}
