from models import User, db, Course, Admin
from app import create_app
from datetime import datetime


app = create_app()


with app.app_context():
    users = [{
        "id": 1,
        "username": "frowlett0",
        "password": "aG0)%",
        "role": "Construction Expeditor",
        "created_at": "3/18/2023",
        "updated_at": "12/26/2023"
    }, {
        "id": 2,
        "username": "ibernaciak1",
        "password": "zZ9?y",
        "role": "Estimator",
        "created_at": "4/15/2023",
        "updated_at": "1/1/2024"
    }, {
        "id": 3,
        "username": "djosilowski2",
        "password": "qJ3)}h=",
        "role": "Estimator",
        "created_at": "8/8/2023",
        "updated_at": "8/27/2023"
    }, {
        "id": 4,
        "username": "kfoulcher3",
        "password": "wW9$ET0Z~",
        "role": "Construction Foreman",
        "created_at": "3/23/2023",
        "updated_at": "5/18/2023"
    }, {
        "id": 5,
        "username": "charroll4",
        "password": "lZ7_,\"!k_",
        "role": "Subcontractor",
        "created_at": "12/20/2023",
        "updated_at": "12/11/2023"
    }, {
        "id": 6,
        "username": "bedlin5",
        "password": "lL1,pTLU",
        "role": "Construction Manager",
        "created_at": "7/24/2023",
        "updated_at": "5/9/2023"
    }, {
        "id": 7,
        "username": "eberi6",
        "password": "uO0\"H&",
        "role": "Architect",
        "created_at": "7/15/2023",
        "updated_at": "11/10/2023"
    }, {
        "id": 8,
        "username": "esammut7",
        "password": "hM2@I}n",
        "role": "Subcontractor",
        "created_at": "3/13/2023",
        "updated_at": "3/6/2023"
    }, {
        "id": 9,
        "username": "dshires8",
        "password": "jK2\\YjKNE",
        "role": "Construction Worker",
        "created_at": "6/6/2023",
        "updated_at": "7/25/2023"
    }, {
        "id": 10,
        "username": "collington9",
        "password": "pC8%c&)I",
        "role": "Estimator",
        "created_at": "2/28/2023",
        "updated_at": "8/6/2023"
    }]

    for user_data in users:
        user_data["created_at"] = datetime.strptime(
            user_data["created_at"], "%m/%d/%Y")
        user_data["updated_at"] = datetime.strptime(
            user_data["updated_at"], "%m/%d/%Y")

        user = User(**user_data)
        db.session.add(user)
    db.session.commit()
    print("Users added!!!")
