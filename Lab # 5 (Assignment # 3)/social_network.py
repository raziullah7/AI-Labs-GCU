class Person:
    def __init__(self, name):
        self.name = name
        self.relationships = {}

    def add_relationship(self, person, relation):
        self.relationships[person] = relation

class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, person):
        self.people[person.name] = person

    def add_relation(self, person1_name, person2_name, relation):
        person1 = self.people.get(person1_name)
        person2 = self.people.get(person2_name)
        if person1 and person2:
            person1.add_relationship(person2, relation)
            person2.add_relationship(person1, relation)

    def get_relation(self, person1_name, person2_name):
        person1 = self.people.get(person1_name)
        person2 = self.people.get(person2_name)
        if person1 and person2:
            relation = self.find_relation(person1, person2)
            if relation:
                return f"{person1_name} - {relation} - {person2_name}"
            else:
                return "No relation found."
        else:
            return "Person not found."

    def find_relation(self, person1, person2):
        visited = set()
        queue = [(person1, "")]
        
        while queue:
            current_person, relation_so_far = queue.pop(0)
            if current_person == person2:
                return relation_so_far
            
            visited.add(current_person)
            for friend, relation in current_person.relationships.items():
                if friend not in visited:
                    queue.append((friend, f"{relation_so_far}<-{relation}->"))
        
        return None

# Creating people
ali = Person("Ali")
ahmad = Person("Ahmad")
yasir = Person("Yasir")
alia = Person("Alia")
ayesha = Person("Ayesha")

# Creating social network
social_network = SocialNetwork()
social_network.add_person(ali)
social_network.add_person(ahmad)
social_network.add_person(yasir)
social_network.add_person(alia)
social_network.add_person(ayesha)

# Adding relations
social_network.add_relation("Ali", "Ahmad", "brotherof")
social_network.add_relation("Ali", "Yasir", "boss of")
social_network.add_relation("Yasir", "Alia", "wife of")
social_network.add_relation("Ahmad", "Ayesha", "colleague of")

# Getting relations
print(social_network.get_relation("Ali", "Ahmad"))  # Output: Ali - brotherof - Ahmad
print(social_network.get_relation("Ayesha", "Alia"))  # Output: Ayesha - colleague of - Ahmad<-boss of - Yasir<-wife of - Alia