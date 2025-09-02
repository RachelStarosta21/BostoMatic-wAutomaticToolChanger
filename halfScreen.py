#making a half screen launcher option for axis

w = root_window.winfo_screenwidth()
h = root_window.winfo_screenheight()

half_width = w // 2
partial_h = h * 0.8
#small = w * 0.03
geometry_str = "%dx%d+0+0" % (half_width, partial_h)
root_window.tk.call("wm", "geometry", ".", geometry_str)

#minimum window size


#wooohoooo