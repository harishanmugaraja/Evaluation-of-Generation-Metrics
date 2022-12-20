from app import app

# to test, cd to api and run:
# pytest

# Sometimes, test_rank_groups() or test_bin_groups() will fail with:
#
# FAILED test_study.py::test_grid_single - KeyError: 'frechet_inception_distance'
# FAILED test_study.py::test_bin_groups - KeyError: 'frechet_inception_distance'
# 
# but other times, either or both pass
# I cannot determine why this is at the moment

app.testing = True
client = app.test_client()

# tests for the expected status code and message from @app.route('/')
def test_index_route():
    response = client.get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Flask server is running!"

# tests for the expected status code from @app.route('/rankGroups')
# tests for the expected number of groups from @app.route('/rankGroups')
# tests for the expected number of images per group from @app.route('/rankGroups')
def test_rank_groups():
    num_groups = 4
    num_imgs = 4
    response = client.get('/rankGroups')

    assert response.status_code == 200
    assert len(response.json["imagearrs"]) == num_groups
    assert len(response.json["imagearrs"][0]["imagelist"]) == num_imgs

# tests for the expected status code from @app.route('/gridWhole')
# tests for the expected number of groups from @app.route('/gridWhole')
# tests for the expected number of images per group from @app.route('/gridWhole')
def test_grid_whole():
    num_groups = 2
    num_imgs = 9
    response = client.get('/gridWhole')

    assert response.status_code == 200

    for i in range(num_groups - 1):
        assert len(response.json["imagearrs"][i]) == num_imgs

# tests for the expected status code from @app.route('/gridSingle')
# tests for the expected number of images from @app.route('/gridSingle')
# tests for the expected number of images per group from @app.route('/gridSingle')
def test_grid_single():
    num_imgs = 9
    fid1 = -1.0
    fid2 = -1.0
    count1 = 0
    count2 = 0
    response = client.get('/gridSingle')

    for im in response.json["groups"]:
        if fid1 == -1.0 and fid2 == -1.0:
            fid1 = im["fid"]
            count1 = 1
        elif im["fid"] == fid1:
            count1 = count1 + 1
        elif im["fid"] == fid2:
            count2 = count2 + 1
        else:
            fid2 = im["fid"]
            count2 = 1

    assert response.status_code == 200
    assert len(response.json["groups"]) == num_imgs
    assert count1 == 8 or count2 == 8

# tests for the expected status code from @app.route('/binGroups')
# tests for the expected number of groups from @app.route('/binGroups')
# tests for the expected number of images per group from @app.route('/binGroups')
def test_bin_groups():
    num_groups = 2
    num_imgs = 4
    response = client.get('/binGroups')

    assert response.status_code == 200
    assert len(response.json["imagearrs"]) == num_groups
    assert len(response.json["imagearrs"][0]["imagelist"]) == num_imgs