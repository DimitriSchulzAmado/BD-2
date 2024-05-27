

def main():
    uri = "neo4j+s://629ae45d.databases.neo4j.io"
    user = "neo4j"
    password = "3ZsZtTP-cPZi23Dvhg_S_lCJIhK6VLnk9sCm_Xy8RzU"
    
    db = Database(uri, user, password)
    
    try:
        # Query 1
        print("Query 1 - Teacher Renzo:")
        renzo = db.get_teacher_by_name("Renzo")
        if renzo:
            print(f"Ano de Nascimento: {renzo['ano_nasc']}, CPF: {renzo['cpf']}")
        else:
            print("Professor não encontrado.")

        # Query 2
        print("\nQuery 2 - Teachers with name starting with 'M':")
        teachers_m = db.get_teachers_by_name_starting_with("M")
        for teacher in teachers_m:
            print(f"Name: {teacher['name']}, CPF: {teacher['cpf']}")

        # Query 3
        print("\nQuery 3 - All City Names:")
        city_names = db.get_all_city_names()
        for name in city_names:
            print(name)

        # Query 4
        print("\nQuery 4 - Schools with number between 150 and 550:")
        schools = db.get_schools_with_number_range(150, 550)
        for school in schools:
            print(f"Name: {school['name']}, Address: {school['address']}, Number: {school['number']}")
    finally:
        db.close()
    

if __name__ == "__main__":
    main()