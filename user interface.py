import tkinter as tk

class StartScreen:
	def __init__(self, root):
		self.root = root
		self.root.geometry("800x600")
		
		self.menuBtn = tk.Button(self.root, text = "menu", command = self.menuWindow)
		self.menuBtn.place(y=20, x=720, width=50, height=50)

	def menuWindow(self):
		newWindow = tk.Toplevel(self.root)
		screen = Menu(newWindow)

class Menu:
	def __init__(self, root):
		root.title("Menu")
		root.geometry("800x600")
		self.root = root
		
		self.countdownBtn = tk.Button(self.root, text = "countdown", command = self.countdownWindow)
		self.countdownBtn.place(y=50, x=400, width=100, height = 50)
		
		self.progressMonitorBtn = tk.Button(self.root, text = "progress monitor", command = self.progressMonitorWindow)
		self.progressMonitorBtn.place(y=120, x = 400, width = 100, height=50)
		
		#self.shopBtn =
		
		#self.lifeEventsBtn = 
		
	def countdownWindow(self):
		countdownScreen = tk.Toplevel(self.root)
		screen = Countdown(countdownScreen)
	
	def progressMonitorWindow(self):
		progressScreen = tk.Toplevel(self.root)
		screen = ProgressMonitor(progressScreen)
		
class Countdown:
		def __init__(self, root):
			root.title("Countdown")
			root.geometry("800x600")
			self.root = root

class ProgressMonitor:
			def __init__(self, root):
				root.title("Progress Monitor")
				root.geometry("800x600")
				self.root = root
	



root = tk.Tk()
object = StartScreen(root)
root.mainloop()
