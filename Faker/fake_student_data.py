from faker import Faker

# Create Faker object
fake = Faker("en_IN")

print("=" * 80)
print("              STUDENT DATA GENERATOR")
print("=" * 80)

# Generate 10 fake student records
for i in range(1, 11):
    print(f"\nStudent {i}")
    print("-" * 40)
    print("Student ID :", fake.random_int(min=1001, max=9999))
    print("Name       :", fake.name())
    print("Age        :", fake.random_int(min=18, max=25))
    print("Gender     :", fake.random_element(elements=("Male", "Female")))
    print("Email      :", fake.email())
    print("Phone      :", fake.phone_number())
    print("Address    :", fake.address())
    print("College    :", "Garden City University")
    print("Course     :", "B.Tech CSE")