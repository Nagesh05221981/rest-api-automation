import uuid
from helpers.api_client import APIClient
from helpers.validators import validate_schema
from schemas.task_schema import task_schema
from schemas.get_task_schema import get_task_schema
from schemas.List_task_schema import list_tasks_schema

def test_get_task(client, endpoints):
    response = client.get( endpoints["health"])
    assert response.status_code == 200
    data = response.json()
    print(data)
def test_create_task(client,endpoints,payloads):
    payload= payloads["sample_task"].copy()
    payload["task_id"] = str(uuid.uuid4())
    response = client.put( endpoint=endpoints["create_task"],json=payload)
    assert response.status_code == 200
    data = response.json()
    validate_schema(data,task_schema)
    #print(data)
    task = data["task"]
    assert task["content"] == payloads["sample_task"]["content"]
    assert task["user_id"] == payloads["sample_task"]["user_id"]
    assert isinstance(task["task_id"], str) and len(task["task_id"]) > 0
    assert task["task_id"] != payloads["sample_task"]["task_id"]  # should be different from placeholder

def test_get_task_by_id(client,endpoints,payloads):
    payload= payloads["sample_task"].copy()
    #payload["task_id"] = str(uuid.uuid4())
    create_task_response = client.put( endpoint=endpoints["create_task"],json=payload)
    assert create_task_response.status_code == 200
    created_task_response = create_task_response.json()["task"]
    #task = created_task_response["task"]
    created_task_id=created_task_response["task_id"]
    #print(created_task_response)
    # Step 2: GET the task by ID
    get_response_by_id =client.get( endpoint=endpoints["get_task"].format(task_id=created_task_id) )
    assert get_response_by_id.status_code == 200
    get_response_data=get_response_by_id.json()
    print(get_response_data)
    # Step3: Validate schema
    validate_schema(get_response_data  ,get_task_schema)


def test_list_tasks(client, endpoints, payloads):
        # Step 1: Create a task
        payload = payloads["sample_task"].copy()
        payload["task_id"] = str(uuid.uuid4())
        payload["user_id"] = "test_user"

        create_resp = client.put(
            endpoint=endpoints["create_task"],
            json=payload
        )
        assert create_resp.status_code == 200

        # Step 2: List tasks
        list_resp = client.get(
            endpoint=endpoints["list_tasks"].format(user_id=payload["user_id"])
        )
        assert list_resp.status_code == 200

        data = list_resp.json()

        # Step 3: Schema validation
        validate_schema(data, list_tasks_schema)

        # Step 4: Data validation
        tasks = data["tasks"]
        assert len(tasks) > 0

        for task in tasks:
            assert task["user_id"] == payload["user_id"]
            assert isinstance(task["task_id"], str)
            assert task["content"]
            assert isinstance(task["created_time"], int)
            assert isinstance(task["ttl"], int)
def test_update_task(client,endpoints,payloads):
    # ---------- Step 1: Create Task ----------
    payload = payloads["sample_task"].copy()
    create_response = client.put( endpoint=endpoints["create_task"],json=payload)
    assert create_response.status_code == 200
    created_task =create_response.json()["task"]
    task_id = created_task["task_id"]
    print(task_id)

    # ---------- Step 2: Get Task by ID ----------
    get_response = client.get( endpoint=endpoints["get_task"].format(task_id=payload["task_id"]))
    assert get_response.status_code == 200
    #print (get_response.json())
    #get_task=get_response.json()
    #assert get_task["task_id"] == task_id

    # -------------Ste 3: Update Task -------------
    update_payload = {
        "task_id": task_id,
        "user_id": payload["user_id"],
        "content": "updated content",
        "is_done": True
    }
    update_task_response = client.put( endpoint=endpoints["update_task"],json=update_payload)
    assert update_task_response.status_code == 200

    # -------------------validate the content is updated ------------
    get_response = client.get(
        endpoint=endpoints["get_task"].format(task_id=task_id)
    )

    assert get_response.status_code == 200

    updated_task = get_response.json()

    # ---------- Step 4: Validate ----------
    assert updated_task["task_id"] == task_id
    assert updated_task["content"] == "updated content"







