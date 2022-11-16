from src.sorting import sort_by

all_jobs = [
    {
        "title": "developer1",
        "min_salary": 3000,
        "max_salary": 4000,
        "date_posted": "2022-16-11"
    },
    {
        "title": "developer2",
        "min_salary": 4000,
        "max_salary": 5000,
        "date_posted": "2022-12-12"
    },
]

result_min_salary = [
    {
        "title": "developer1",
        "min_salary": 3000,
        "max_salary": 4000,
        "date_posted": "2022-16-11"
    },
    {
        "title": "developer2",
        "min_salary": 4000,
        "max_salary": 5000,
        "date_posted": "2022-12-12"
    },
]

result_max_salary = [
    {
        "title": "developer2",
        "min_salary": 4000,
        "max_salary": 5000,
        "date_posted": "2022-12-12"
    },
    {
        "title": "developer1",
        "min_salary": 3000,
        "max_salary": 4000,
        "date_posted": "2022-16-11"
    },
]

result_date_posted = [
    {
        "title": "developer2",
        "min_salary": 4000,
        "max_salary": 5000,
        "date_posted": "2022-12-12"
    },
    {
        "title": "developer1",
        "min_salary": 3000,
        "max_salary": 4000,
        "date_posted": "2022-16-11"
    },
]


def test_sort_by_criteria():
    sort_by(all_jobs, "min_salary")
    assert all_jobs == result_min_salary
    sort_by(all_jobs, "max_salary")
    assert all_jobs == result_max_salary
    sort_by(all_jobs, "date_posted")
    assert all_jobs == result_date_posted
