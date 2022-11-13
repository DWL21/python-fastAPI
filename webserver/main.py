from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Member(BaseModel):
    member_id: int
    name: str

    def update_name(self, name: str):
        self.name = name


@app.get("/")
def root() -> dict[str, str]:
    return {"text": "Hello World"}


@app.post("/members", status_code=201)
def create(name: str) -> Member:
    return save(name)


@app.get("/members/{member_id}")
def read(member_id: int) -> Member:
    return find_member(member_id)


@app.get("/members")
def read() -> dict[str, list[Member]]:
    return {"data": find_all()}


@app.put("/members/{member_id}")
def update(member_id: int, name: str) -> Member:
    return update_member(member_id, name)


@app.delete("/members/{member_id}", status_code=204)
def delete(member_id: int) -> None:
    delete_member(member_id)


members: dict[int, Member] = dict()


def save(this_name: str) -> Member:
    member: Member = Member(member_id=len(members) + 1, name=this_name)
    members[member.member_id] = member
    return members[member.member_id]


def find_member(member_id: int) -> Member:
    return members[member_id]


def find_all() -> list[Member]:
    return list(members.values())


def update_member(member_id: int, name: str) -> Member:
    member: Member = find_member(member_id)
    member.update_name(name)
    return member


def delete_member(member_id: int) -> None:
    members.pop(member_id)
