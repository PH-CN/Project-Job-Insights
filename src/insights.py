from src.jobs import read


def get_unique_job_types(path):
    result = list()
    jobs = read(path)

    for job in jobs:
        if job["job_type"] not in result:
            result.append(job["job_type"])

    return result
    # """Checks all different job types and returns a list of them

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # list
    #     List of unique job types
    # """


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]
    # """Filters a list of jobs by job_type

    # Parameters
    # ----------
    # jobs : list
    # job_type : str
    #     Industry for the list filter

    # Returns
    # -------
    # list
    #     List of jobs with provided job_type
    # """


def get_unique_industries(path):
    industries = list()
    jobs = read(path)

    for job in jobs:
        if job["industry"] not in industries:
            if job["industry"] != "":
                industries.append(job["industry"])

    return industries
    # """Checks all different industries and returns a list of them

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # list
    #     List of unique industries
    # """


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]
    # """Filters a list of jobs by industry

    # Parameters
    # ----------
    # jobs : list
    # industry : str
    #     Industry for the list filter

    # Returns
    # -------
    # list
    #     List of jobs with provided industry
    # """


def get_max_salary(path):
    jobs = read(path)
    max_salary = 0
    for job in jobs:
        if job["max_salary"].isdigit() and int(job["max_salary"]) > max_salary:
            max_salary = int(job["max_salary"])

    return max_salary
    # """Get the maximum salary of all jobs

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # int
    #     The maximum salary paid out of all job opportunities
    # """


def get_min_salary(path):
    jobs = read(path)
    min_salary = 1000000000
    for job in jobs:
        if job["min_salary"].isdigit() and int(job["min_salary"]) < min_salary:
            min_salary = int(job["min_salary"])

    return min_salary
    # """Get the minimum salary of all jobs

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # int
    #     The minimum salary paid out of all job opportunities
    # """


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("max_salary or min_salary are missing")
    elif type(job["max_salary"]) != int or type(job["min_salary"]) != int:
        raise ValueError("max_salary or min_salary are not ints")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary is greather than max_salary")
    elif type(salary) != int:
        raise ValueError("salary is not an int")
    else:
        return job["min_salary"] <= salary < job["max_salary"]

        # """Checks if a given salary is in the salary range of a given job

        # Parameters
        # ----------
        # job : dict
        #     The job with `min_salary` and `max_salary` keys
        # salary : int
        #     The salary to check if matches with salary range of the job

        # Returns
        # -------
        # bool
        #     True if the salary is in the salary range of the job, False otherwise

        # Raises
        # ------
        # ValueError
        #     If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        #     If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        #     If `job["min_salary"]` is greather than `job["max_salary"]`
        #     If `salary` isn't a valid integer
        print(salary)
    # """


def filter_by_salary_range(jobs, salary):
    try:
        result = []
        for job in jobs:
            if (
                type(job["max_salary"]) == int
                and type(job["min_salary"]) == int
                and job["max_salary"] > job["min_salary"]
            ):
                if matches_salary_range(job, salary):
                    result.append(job)
        return result
    except ValueError:
        return []
    # """Filters a list of jobs by salary range

    # Parameters
    # ----------
    # jobs : list
    #     The jobs to be filtered
    # salary : int
    #     The salary to be used as filter

    # Returns
    # -------
    # list
    #     Jobs whose salary range contains `salary`
    # """
