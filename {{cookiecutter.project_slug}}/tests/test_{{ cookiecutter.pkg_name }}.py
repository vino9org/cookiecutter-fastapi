async def test_probes(client) -> None:
    response = await client.get("/healthz")
    assert response.status_code == 200

    response = await client.get("/ready")
    assert response.status_code == 200


# async def test_get_users(client) -> None:
#     response = await client.get("/users")
#     assert response.status_code == 200
#     assert response.json() == []
