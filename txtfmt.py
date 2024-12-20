import tkinter as tk

def split_text():
    input_text = InTextbox.get("1.0",tk.END).rstrip()
    output_text = input_text.replace(Entry.get(),split[svar.get()])
    OutTextbox.delete("1.0",tk.END)
    OutTextbox.insert("1.0",output_text)

root = tk.Tk()
root.title("Text Formatter")
root.geometry("480x320")
split = ["\n","\t"]
svar = tk.IntVar()

#elements
FrameL = tk.Frame(root)
FrameR = tk.Frame(root)
Option = tk.LabelFrame(FrameL,text="Option")
FrameS = tk.Frame(Option)
FrameE = tk.Frame(Option)
InLabel = tk.Label(FrameL,text="Paste here")
EntryLabel = tk.Label(FrameE,text="Delimiter:")
OutLabel = tk.Label(FrameR,text="Output")
BottomLabel = tk.Label(root,text="Take care to enter the delimiter.")
Button = tk.Button(FrameL,text="Format!",command=split_text)
Select0 = tk.Radiobutton(FrameS,value=0,
                         variable=svar,text="by row (LF)")
Select1 = tk.Radiobutton(FrameS,value=1,
                         variable=svar,text="by column (Tab)")
Entry = tk.Entry(FrameE)
InTextbox = tk.Text(FrameL,height=10,width=32)
OutTextbox = tk.Text(FrameR,height=21,width=32)

#placement
BottomLabel.pack(side=tk.BOTTOM,anchor=tk.SW)
FrameL.pack(expand=1,fill="x",side="left",anchor=tk.NW)
FrameR.pack(expand=1,fill="x",side="left",anchor=tk.NW)
InLabel.pack(); InTextbox.pack(); Option.pack(pady=10)
FrameE.pack(expand=1,fill="x",side="top",padx=5,pady=5)
EntryLabel.pack(side="left"); Entry.pack(side="left")
FrameS.pack(expand=1,fill="x",side="top",padx=5,pady=5)
Select0.pack(side="left"); Select1.pack(side="left")
Button.pack()
OutLabel.pack(); OutTextbox.pack()

root.mainloop()
