import tkinter as tk


if __name__ == "__main__":
    entries = [[],[],[],[]]

    def attrFetch(category, index):
        if category == 'bat':
            result = float(entries[0][index].get())
        elif category == 'pitch':
            result = float(entries[1][index].get())
        elif category == 'base':
            result = float(entries[2][index].get())
        elif category == 'def':
            result = float(entries[3][index].get())
        return result

    def calcBatting():
        batRating = 10*pow(attrFetch('bat', 0), 0.35) * pow(attrFetch('bat', 1), 0.35)* pow(max(1 - attrFetch('bat', 2), 0.01), 0.05) * pow(max(1 - attrFetch('bat', 3), 0.01), 0.05) * pow(attrFetch('bat', 4), 0.075) * pow(attrFetch('bat', 5), 0.075) * pow(attrFetch('bat', 6), 0.02)
        batStars = round(batRating)/2
        batStarsText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=batStars)
        batStarsText.grid(row=0, column=(9))
        batRatingText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=batRating)
        batRatingText.grid(row=0, column=(10))
    def calcPitching():
        pitchRating = 10*pow(attrFetch('pitch', 0), 0.4) * pow(attrFetch('pitch',1), 0.5) * pow(attrFetch('pitch',2), 0.15) * pow(attrFetch('pitch',3), 0.1) * pow(attrFetch('pitch',4), 0.025)
        pitchStars = round(pitchRating)/2
        pitchStarsText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=pitchStars)
        pitchStarsText.grid(row=2, column=(9))
        pitchRatingText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=pitchRating)
        pitchRatingText.grid(row=2, column=(10))
    def calcBaserunning():
        baseRating = 10*pow(attrFetch('base', 0), 0.5) * pow(attrFetch('base', 1), 0.1) * pow(attrFetch('base', 2), 0.1) * pow(attrFetch('base', 3), 0.1) * pow(attrFetch('base', 4), 0.1)
        baseStars = round(baseRating)/2
        baseStarsText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=baseStars)
        baseStarsText.grid(row=4, column=(9))
        baseRatingText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=baseRating)
        baseRatingText.grid(row=4, column=(10))
    def calcDefense():
        defRating = 10*pow(attrFetch('def', 0), 0.2) * pow(attrFetch('def', 1), 0.2) * pow(attrFetch('def', 2), 0.1) * pow(attrFetch('def', 3), 0.1) * pow(attrFetch('def', 4), 0.1)
        defStars = round(defRating)/2
        defStarsText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=defStars)
        defStarsText.grid(row=6, column=(9))
        defRatingText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=defRating)
        defRatingText.grid(row=6, column=(10))

    def maximize(target):
        if target == "Batting":
            batAttr = [attrFetch('bat', 0), attrFetch('bat', 1), attrFetch('bat', 2), attrFetch('bat', 3), attrFetch('bat', 4), attrFetch('bat', 5), attrFetch('bat', 6), attrFetch('bat', 7)]
            batRating = 10*pow(batAttr[0], 0.35) * pow(batAttr[1], 0.35)* pow(max(1 - batAttr[2], 0.01), 0.05) * pow(max(1 - batAttr[3], 0.01), 0.05) * pow(batAttr[4], 0.075) * pow(batAttr[5], 0.075) * pow(batAttr[6], 0.02)
            batStars = round(batRating)/2
            while batStars < 5:
                for index, attr in enumerate(batAttr):
                    if index == 2 or index == 3:
                        batAttr[index] = max(batAttr[index] - 0.01, 0.01)
                    else:
                        batAttr[index] += 0.01
                batRating = 10*pow(batAttr[0], 0.35) * pow(batAttr[1], 0.35)* pow(max(1 - batAttr[2], 0.01), 0.05) * pow(max(1 - batAttr[3], 0.01), 0.05) * pow(batAttr[4], 0.075) * pow(batAttr[5], 0.075) * pow(batAttr[6], 0.02)
                batStars = round(batRating)/2
            batStarsText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=batStars)
            batStarsText.grid(row=0, column=(9))
            batRatingText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=batRating)
            batRatingText.grid(row=0, column=(10))
            for index, entry in enumerate(entries[0]):
                entry.delete('0', 'end')
                entry.insert('insert', round(batAttr[index], 4))
        elif target == "Pitching":
            pitchAttr = [attrFetch('pitch', 0), attrFetch('pitch', 1), attrFetch('pitch', 2), attrFetch('pitch', 3), attrFetch('pitch', 4), attrFetch('pitch', 5)]
            pitchRating = 10*pow(pitchAttr[0], 0.4) * pow(pitchAttr[1], 0.5) * pow(pitchAttr[2], 0.15) * pow(pitchAttr[3], 0.1) * pow(pitchAttr[4], 0.025)
            pitchStars = round(pitchRating)/2
            while pitchStars < 5:
                for index, attr in enumerate(pitchAttr):
                    pitchAttr[index] += 0.01
                pitchRating = 10*pow(pitchAttr[0], 0.4) * pow(pitchAttr[1], 0.5) * pow(pitchAttr[2], 0.15) * pow(pitchAttr[3], 0.1) * pow(pitchAttr[4], 0.025)
                pitchStars = round(pitchRating)/2
            pitchStarsText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=pitchStars)
            pitchStarsText.grid(row=2, column=(9))
            pitchRatingText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=pitchRating)
            pitchRatingText.grid(row=2, column=(10))
            for index, entry in enumerate(entries[1]):
                entry.delete('0', 'end')
                entry.insert('insert', round(pitchAttr[index], 4))
        elif target == "Baserunning":
            baseAttr = [attrFetch('base', 0), attrFetch('base', 1), attrFetch('base', 2), attrFetch('base', 3), attrFetch('base', 4)]
            baseRating = 10*pow(baseAttr[0], 0.5) * pow(baseAttr[1], 0.1) * pow(baseAttr[2], 0.1) * pow(baseAttr[3], 0.1) * pow(baseAttr[4], 0.1)
            baseStars = round(baseRating)/2
            while baseStars < 5:
                for index, attr in enumerate(baseAttr):
                    baseAttr[index] += 0.01
                baseRating = 10*pow(baseAttr[0], 0.5) * pow(baseAttr[1], 0.1) * pow(baseAttr[2], 0.1) * pow(baseAttr[3], 0.1) * pow(baseAttr[4], 0.1)
                baseStars = round(baseRating)/2
            baseStarsText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=baseStars)
            baseStarsText.grid(row=4, column=(9))
            baseRatingText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=baseRating)
            baseRatingText.grid(row=4, column=(10))
            for index, entry in enumerate(entries[2]):
                entry.delete('0', 'end')
                entry.insert('insert', round(baseAttr[index], 4))
        elif target == "Defense":
            defAttr = [attrFetch('def', 0), attrFetch('def', 1), attrFetch('def', 2), attrFetch('def', 3), attrFetch('def', 4)]
            defRating = 10*pow(defAttr[0], 0.2) * pow(defAttr[1], 0.2) * pow(defAttr[2], 0.1) * pow(defAttr[3], 0.1) * pow(defAttr[4], 0.1)
            defStars = round(defRating)/2
            while defStars < 5:
                for index, attr in enumerate(defAttr):
                    defAttr[index] += 0.01
                defRating = 10*pow(defAttr[0], 0.2) * pow(defAttr[1], 0.2) * pow(defAttr[2], 0.1) * pow(defAttr[3], 0.1) * pow(defAttr[4], 0.1)
                defStars = round(defRating)/2
            defStarsText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=defStars)
            defStarsText.grid(row=6, column=(9))
            defRatingText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=defRating)
            defRatingText.grid(row=6, column=(10))
            for index, entry in enumerate(entries[3]):
                entry.delete('0', 'end')
                entry.insert('insert', round(defAttr[index], 4))

    gui = tk.Tk()
    gui.configure(background='light blue')
    gui.title('Stars Calculator')
    gui.geometry('1250x208')

    battingAttrs = ['Thwackability', 'Divinity', 'Patheticism', 'Tragicness', 'Musclitude', 'Moxie', 'Martyrdom', 'Buoyancy']
    pitchingAttrs = ['Ruthlessness', 'Unthwackability', 'Overpowerment', 'Shakespearianism', 'Coldness', 'Suppression']
    baserunningAttrs = ['Laserlikeness', 'Continuation', 'Base Thirst', 'Ground Friction', 'Indulgence']
    defenseAttrs = ['Omniscience', 'Tenaciousness', 'Chasiness', 'Watchfulness', 'Anticapitalism']
    attributes = [battingAttrs, pitchingAttrs, baserunningAttrs, defenseAttrs]

    calc = [['Batting Stars', lambda:calcBatting()], ['Pitching Stars', lambda: calcPitching()], ['Baserunning Stars', lambda: calcBaserunning()], ['Defense Stars', lambda: calcDefense()]]
    maxFunc = [['Max Batting', lambda: maximize("Batting")], ['Max Pitching', lambda: maximize("Pitching")], ['Max Baserunning', lambda: maximize("Baserunning")], ['Max Defense', lambda: maximize("Defense")]]

    for typeIndex, attrType in enumerate(attributes):
        row=(2*typeIndex) 
        calcButtons = tk.Button(gui, text=calc[typeIndex][0], fg='black', bg='light blue', command=calc[typeIndex][1], height=1, width=15)
        calcButtons.grid(sticky='S', row=row, column=0)
        maxButtons = tk.Button(gui, text=maxFunc[typeIndex][0], fg='black', bg='light blue', command=maxFunc[typeIndex][1], height=1, width=15)
        maxButtons.grid(sticky='S', row=row+1, column=0)
        for attrIndex, attr in enumerate(attrType):
            attrBut = tk.Entry(gui, width=5)
            attrBut.insert('insert', '0.5')
            attrBut.grid(row=row, column=(attrIndex+1))
            attrText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text=attr)
            attrText.grid(row=row+1, column=(attrIndex+1))
            entries[typeIndex].append(attrBut)
        starsText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text='Stars')
        starsText.grid(row=row+1, column=(9))
        starsText = tk.Label(gui, height=1, width=15, background='light blue', anchor='center', padx=1, pady=1, text='Rating')
        starsText.grid(row=row+1, column=(10))

    gui.mainloop()

