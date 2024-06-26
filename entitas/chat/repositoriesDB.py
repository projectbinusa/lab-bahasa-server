from pony.orm import *
from database.schema import ChatDB, UserDB, MessageChatDB


@db_session
def get_all_with_pagination_by_class_id(class_id, page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in ChatDB if (s.class_id == class_id)).order_by(desc(ChatDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "content":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.content)

        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error Group getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def get_all_with_pagination_by_class_id_and_sender_id_receiver_id(class_id, sender_id, receiver_id, page=1, limit=9,
                                                                  filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        # Filter berdasarkan class_id, sender_id, dan receiver_id
        data_in_db = select(s for s in ChatDB if
                            s.class_id == class_id and s.sender_id == sender_id and s.receiver_id == receiver_id).order_by(
            desc(ChatDB.id))

        # Terapkan filter tambahan
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: d.id == item["value"])
            elif item["field"] == "content":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.content)
            elif item["field"] == "sender_id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.sender_id)
            elif item["field"] == "receiver_id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.receiver_id)

        # Hitung total record
        total_record = data_in_db.count()

        # Terapkan pagination jika limit lebih dari 0
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)

        # Konversi data ke model atau response
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error pada getAllWithPagination: ", e)

    # Hitung total halaman
    total_page = (total_record + limit - 1) // limit if limit > 0 else 1

    return result, {
        "total": total_record,
        "page": page,
        "total_page": total_page,
    }


@db_session
def get_all_with_pagination_by_class_id_and_topic_chat_id(class_id, topic_chat_id, page=1, limit=9, filters=[],
                                                          to_model=False):
    result = []

    total_record = 0
    try:
        data_in_db = select(s for s in ChatDB if s.class_id == class_id and s.topic_chat_id == topic_chat_id).order_by(
            desc(ChatDB.id))

        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: d.id == item["value"])
            elif item["field"] == "content":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.content)
            elif item["field"] == "class_id":
                data_in_db = data_in_db.filter(lambda d: item["value"] == d.class_id)
            elif item["field"] == "topic_chat_id":
                data_in_db = data_in_db.filter(lambda d: item["value"] == d.topic_chat_id)

        total_record = data_in_db.count()

        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)

        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error getAllWithPaginationByTopicChatId: ", e)

    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def get_all_with_pagination_by_class_id_and_group_id(class_id=0, group_id=0, page=1, limit=9, filters=[], order_by="-created_date", to_model=False):
    data_in_db = select(m for m in ChatDB if m.class_id == class_id and m.group_id == group_id)

    for item in filters:
        if item["field"] == "content":
            data_in_db = data_in_db.filter(lambda d: item["value"] in d.content)
        elif item["field"] == "class_id":
            data_in_db = data_in_db.filter(lambda d: item["value"] == d.class_id)
        elif item["field"] == "group_id":
            data_in_db = data_in_db.filter(lambda d: item["value"] == d.group_id)

    total_record = data_in_db.count()

    if limit > 0:
        if order_by == "-created_date":
            data_in_db = data_in_db.order_by(desc(ChatDB.created_date)).page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db.order_by(ChatDB.created_date).page(pagenum=page, pagesize=limit)

    result = []
    for item in data_in_db:
        if to_model:
            result.append(item.to_model())
        else:
            result.append(item.to_model().to_response())

    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }




@db_session
def update_chat(json_object={}, to_model={}):
    try:
        gambar = json_object.get("gambar", None)
        content = json_object.get("content", None)
        updated_chat = ChatDB[json_object["id"]]
        updated_chat.is_group = json_object["is_group"]
        updated_chat.content = content
        updated_chat.sender_id = json_object["sender_id"]
        updated_chat.class_id = json_object["class_id"]
        updated_chat.gambar = gambar
        commit()
        if to_model:
            print(updated_chat.to_model())
            return updated_chat.to_model()
        else:
            print(updated_chat.to_model().to_response())
            return updated_chat.to_model().to_response()
    except Exception as e:
        print("error Chat update: ", e)
    return None


@db_session
def delete_chat_by_id_and_by_class_id(id=None, class_id=None):
    try:
        ChatDB.get(id=id, class_id=class_id).delete()
        commit()
        return True
    except Exception as e:
        print("error Chat delete: ", e)
    return


# @db_session
# def insert_private_chat(receiver_id, json_object={}, to_model=False):
#     print(receiver_id)
#     try:
#         new_chat = ChatDB(
#             class_id=json_object["class_id"],
#             sender_id=json_object["sender_id"],
#             receiver_id=int(receiver_id),
#             content=json_object["content"],
#             is_group=json_object["is_group"],
#             gambar=json_object["gambar"]
#         )
#         commit()
#         if to_model:
#             return new_chat.to_model()
#         else:
#             return new_chat.to_model().to_response()
#     except Exception as e:
#         print("error Chat insert: ", e)
#     return None

@db_session
def insert_private_chat(receiver_id, json_object={}, to_model=False):
    print(receiver_id)
    try:
        gambar = json_object.get("gambar", None)
        content = json_object.get("content", None)
        new_chat = ChatDB(
            class_id=json_object["class_id"],
            sender_id=json_object["sender_id"],
            receiver_id=int(receiver_id),
            content=content,
            is_group=json_object["is_group"],
            gambar=gambar
        )
        commit()
        if to_model:
            return new_chat.to_model()
        else:
            return new_chat.to_model().to_response()
    except Exception as e:
        print("error Chat insert: ", e)
    return None


@db_session
def insert_group_chat(group_id, json_object={}, to_model=False):
    try:
        gambar = json_object.get("gambar", None)
        content = json_object.get("content", None)

        new_chat = ChatDB(
            class_id=json_object["class_id"],
            sender_id=json_object["sender_id"],
            group_id=int(group_id),
            content=content,
            is_group=json_object["is_group"],
            gambar=gambar
        )
        commit()
        if to_model:
            return new_chat.to_model()
        else:
            return new_chat.to_model().to_response()
    except Exception as e:
        print("error Chat insert: ", e)
    return None


@db_session
def insert_topic_chat(topic_chat_id, json_object={}, to_model=False):
    try:
        gambar = json_object.get("gambar", None)
        content = json_object.get("content", None)

        new_chat = ChatDB(
            class_id=json_object["class_id"],
            sender_id=json_object["sender_id"],
            topic_chat_id=int(topic_chat_id),
            content=content,
            is_group=json_object["is_group"],
            gambar=gambar
        )
        commit()
        if to_model:
            return new_chat.to_model()
        else:
            return new_chat.to_model().to_response()
    except Exception as e:
        print("error Chat insert: ", e)
    return None


@db_session
def get_chats_for_user(user_id, sender_id=None):
    try:
        if sender_id:
            chats = select(m for m in ChatDB if (m.receiver_id == user_id and m.sender_id == sender_id) or
                           (m.receiver_id == sender_id and m.sender_id == user_id))
        else:
            chats = select(m for m in ChatDB if m.receiver_id == user_id or m.sender_id == user_id)
        return [m.to_model() for m in chats]
    except Exception as e:
        print("error getting chats for user: ", e)
        return []

# @db_session
# def add_user_to_chat(chat_id, user_id):
#     chat = ChatDB.get(id=chat_id)
#     user = UserDB.get(id=user_id)
#     chat.users.add(user)
#     commit()


# @db_session
# def create_message(sender_id, chat_id, content):
#     message = MessageChatDB.get(sender_id=sender_id, chat_id=chat_id, content=content)
#     commit()
#     return message


# @db_session
# def create_chat(name, is_group):
#     return ChatDB(name=name, is_group=is_group)

# @db_session
# def add_user_to_chat(chat_id, user_id):
#     chat = ChatDB.get(id=chat_id)
#     user = UserDB.get(id=user_id)
#     chat.users.add(user)

# @db_session
# def
@db_session
def get_chat(chat_id):
    return ChatDB.get(id=chat_id)


@db_session
def get_user_chats(user_id):
    user = UserDB.get(id=user_id)
    return user.private_chats + user.group_chats


@db_session
def find_by_chat_by_message_id(chat=None, user_id=0):
    data_in_db = select(s for s in ChatDB if s.chat == chat and s.user_id == user_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in ChatDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def get_by_class_id(class_id=None):
    data_in_db = select(s for s in ChatDB if s.class_id == class_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def get_by_sender_id(sender_id=None):
    data_in_db = select(s for s in ChatDB if s.sender_id == sender_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def get_by_receiver_id(receiver_id=0):
    data_in_db = select(s for s in ChatDB if s.receiver_id == receiver_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def get_by_topic_chat_id(topic_chat_id=None):
    data_in_db = select(s for s in ChatDB if s.topic_chat_id == topic_chat_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def get_by_group_id(group_id=None, order_by="-created_date"):
    data_in_db = select(m for m in ChatDB if m.group_id == group_id).order_by(desc(ChatDB.created_date))
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def delete_chat_by_group_id_and_class_id(id=None, group_id=None, class_id=None):
    try:
        chat_entry = ChatDB.get(id=id, group_id=group_id, class_id=class_id)
        if chat_entry:
            chat_entry.delete()
            commit()
            return True
        else:
            print(f"No chat entry found with group_id={group_id} and class_id={class_id}")
    except Exception as e:
        print("error Chat delete: ", e)
    return False


@db_session
def get_chat_by_id_and_by_group_id_and_by_class_id(id=None, group_id=None, class_id=None):
    data_in_db = select(s for s in ChatDB if s.id == id and s.group_id == group_id and s.class_id == class_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def insert_receiver_chat(receiver_id, json_object={}, to_model=False):
    try:
        gambar = json_object.get("gambar", None)
        content = json_object.get("content", None)

        new_chat = ChatDB(
            class_id=json_object["class_id"],
            sender_id=json_object["sender_id"],
            receiver_id=int(receiver_id),
            content=content,
            gambar=gambar
        )
        commit()
        if to_model:
            return new_chat.to_model()
        else:
            return new_chat.to_model().to_response()
    except Exception as e:
        print("error Chat insert: ", e)
    return None

@db_session
def update_chat_by_receiver_id_and_class_id(json_object={}, to_model=False):
    try:
        updated_chat = ChatDB[json_object["id"]]
        updated_chat.content = json_object["content"]
        updated_chat.class_id = json_object["class_id"]
        if json_object["gambar"] is not None:
            updated_chat.gambar = json_object["gambar"]
        else:
            print("gambar is None or not provided")

        commit()
        if to_model:
            print(updated_chat.to_model())
            return updated_chat.to_model()
        else:
            print(updated_chat.to_model().to_response())
            return updated_chat.to_model().to_response()
    except Exception as e:
        print("error Chat di repositories update: ", e)
    return None

@db_session
def get_all_with_pagination_by_class_id_and_receiver_id(class_id=0, receiver_id=0, page=1, limit=9, filters=[], order_by="-created_date", to_model=False):
    data_in_db = select(m for m in ChatDB if m.class_id == class_id and m.receiver_id == receiver_id)

    for item in filters:
        if item["field"] == "content":
            data_in_db = data_in_db.filter(lambda d: item["value"] in d.content)
        elif item["field"] == "class_id":
            data_in_db = data_in_db.filter(lambda d: item["value"] == d.class_id)
        elif item["field"] == "receiver_id":
            data_in_db = data_in_db.filter(lambda d: item["value"] == d.receiver_id)

    total_record = data_in_db.count()

    if limit > 0:
        if order_by == "-created_date":
            data_in_db = data_in_db.order_by(desc(ChatDB.created_date)).page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db.order_by(ChatDB.created_date).page(pagenum=page, pagesize=limit)

    result = []
    for item in data_in_db:
        if to_model:
            result.append(item.to_model())
        else:
            result.append(item.to_model().to_response())

    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def delete_chat_by_receiver_id_and_class_id(id=None, receiver_id=None, class_id=None):
    try:
        chat_entry = ChatDB.get(id=id, receiver_id=receiver_id, class_id=class_id)
        if chat_entry:
            chat_entry.delete()
            commit()
            return True
        else:
            print(f"No chat entry found with receiver_id={receiver_id} and class_id={class_id}")
    except Exception as e:
        print("error Chat delete: ", e)
    return False


@db_session
def delete_chat_by_topic_chat_id_and_class_id(id=None, topic_chat_id=None, class_id=None):
    try:
        chat_entry = ChatDB.get(id=id, topic_chat_id=topic_chat_id, class_id=class_id)
        if chat_entry:
            chat_entry.delete()
            commit()
            return True
        else:
            print(f"No chat entry found with topic_chat_id={topic_chat_id} and class_id={class_id}")
    except Exception as e:
        print("error Chat delete: ", e)
    return False


