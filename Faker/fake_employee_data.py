from faker import Faker
import random

# Create Faker object
fake = Faker("en_IN")

print("=" * 90)
print("                     EMPLOYEE DATA GENERATOR")
print("=" * 90)

departments = [
    "HR",
    "Finance",
    "IT",
    "Marketing",
    "Sales",
    "Testing",
    "Development",
    "Support"
]

designations = [
    "Software Engineer",
    "QA Engineer",
    "Senior Developer",
    "System Analyst",
    "Project Manager",
    "HR Executive",
    "Business Analyst",
    "Technical Support"
]

# Generate 10 fake employee records
for i in range(1, 11):
    employee_id = "EMP" + str(random.randint(1000, 9999))
    salary = random.randint(25000, 120000)

    print("\nEmployee", i)
    print("-" * 50)
    print("Employee ID   :", employee_id)
    print("Name          :", fake.name())
    print("Gender        :", random.choice(["Male", "Female"]))
    print("Age           :", random.randint(22, 55))
    print("Department    :", random.choice(departments))
    print("Designation   :", random.choice(designations))
    print("Salary        : Rs.", salary)
    print("Email         :", fake.company_email())
    print("Phone         :", fake.phone_number())
    print("Company       :", fake.company())
    print("Joining Date  :", fake.date_between(start_date="-10y", end_date="today"))
    print("City          :", fake.city())

print("\n" + "=" * 90)
print("Successfully Generated 10 Fake Employee Records")
print("=" * 90)