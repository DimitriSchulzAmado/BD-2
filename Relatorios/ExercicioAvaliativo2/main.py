from src.query import Database
from src.teacher_crud import TeacherCRUD

def main():
    uri = "neo4j+s://629ae45d.databases.neo4j.io"
    user = "neo4j"
    password = "3ZsZtTP-cPZi23Dvhg_S_lCJIhK6VLnk9sCm_Xy8RzU"
    
    db = Database(uri, user, password)
    teacher_crud = TeacherCRUD(db)

    try:
        # Question 1 - Queries
        print("Query 1 - Teacher Renzo:")
        renzo = db.get_teacher_by_name("Renzo")
        if renzo:
            print(f"Ano de Nascimento: {renzo['ano_nasc']}, CPF: {renzo['cpf']}")
        else:
            print("Professor não encontrado.")

        print("\nQuery 2 - Teachers with name starting with 'M':")
        teachers_m = db.get_teachers_by_name_starting_with("M")
        for teacher in teachers_m:
            print(f"Name: {teacher['name']}, CPF: {teacher['cpf']}")

        print("\nQuery 3 - All City Names:")
        city_names = db.get_all_city_names()
        for name in city_names:
            print(name)

        print("\nQuery 4 - Schools with number between 150 and 550:")
        schools = db.get_schools_with_number_range(150, 550)
        for school in schools:
            print(f"Name: {school['name']}, Address: {school['address']}, Number: {school['number']}")

        # Question 2 - Queries
        print("\nQuery 5 - Oldest and Youngest Teacher:")
        age_range = db.get_oldest_and_youngest_teacher()
        print(f"Mais Velho: {age_range['mais_velho']}, Mais Jovem: {age_range['mais_jovem']}")

        print("\nQuery 6 - Average Population:")
        average_population = db.get_average_population()
        print(f"Média de População: {average_population['media_populacao']}")

        print("\nQuery 7 - City with CEP 37540-000:")
        city = db.get_city_by_cep("37540-000")
        if city:
            print(f"Nome da Cidade: {city['name']}")
        else:
            print("Cidade não encontrada.")

        print("\nQuery 8 - Third Character of Teacher Names:")
        third_chars = db.get_third_char_of_teacher_names()
        for char in third_chars:
            print(char['char'])

        # Question 3 - Teacher CRUD
        teacher_crud.create('Chris Lima', 1956, '189.052.396-66')
        print("Professor Chris Lima criado.")

        print("\nLendo o professor Chris Lima:")
        chris = teacher_crud.read('Chris Lima')
        print(f"Name: {chris['name']}, Ano de Nascimento: {chris['ano_nasc']}, CPF: {chris['cpf']}")

        teacher_crud.update('Chris Lima', '162.052.777-77')
        print("\nCPF do professor Chris Lima atualizado.")

        print("\nLendo o professor Chris Lima atualizado:")
        chris_updated = teacher_crud.read('Chris Lima')
        print(f"Name: {chris_updated['name']}, Ano de Nascimento: {chris_updated['ano_nasc']}, CPF: {chris_updated['cpf']}")

        teacher_crud.delete('Chris Lima')
        print("\nProfessor Chris Lima deletado.")

        print("\nVerificando a deleção do professor Chris Lima:")
        chris_deleted = teacher_crud.read('Chris Lima')
        if chris_deleted:
            print(f"Name: {chris_deleted['name']}, Ano de Nascimento: {chris_deleted['ano_nasc']}, CPF: {chris_deleted['cpf']}")
        else:
            print("Professor Chris Lima não encontrado.")
    finally:
        db.close()

if __name__ == "__main__":
    main()