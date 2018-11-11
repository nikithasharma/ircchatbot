import random
philosophical={
    "Nietzsche":    ["He who has a why to live can bear almost any how",
                    "To live is to suffer, to survive is to find some meaning in the suffering",
                    "Without music, life would be a mistake.",
                    "That which does not kill us makes us stronger"],
    
    "Freud":        ["Sometimes a cigar is just a cigar.",
                    "From error to error one discovers the entire truth.",
                    "One day, in retrospect, the years of struggle will strike you as the most beautiful.",
                    "Dreams are often most profound when they seem the most crazy."],
    
    "Marx":         ["The philosophers have only interpreted the world, in various ways. The point, however, is to change it.",
                    "Men make their own history, but they do not make it as they please.",
                    "History repeats itself, first as tragedy, second as farce.",
                    "Reason has always existed, but not always in a reasonable form."],
    
    "Kierkegaard":  ["Life can only be understood backwards; but it must be lived forwards.",
                    "Life is not a problem to be solved, but a reality to be experienced.",
                    "Anxiety is the dizziness of freedom.",
                    "People understand me so poorly that they don't even understand my complaint about them not understanding me."]}

print(random.choice(philosophical["Marx"])," - Karl Marx")
print(random.choice(philosophical["Freud"])," - Sigmund Freud")
print(random.choice(philosophical["Kierkegaard"])," - Søren Kierkegaard")
print(random.choice(philosophical["Nietzsche"])," - Friedrich Nietzsche")
