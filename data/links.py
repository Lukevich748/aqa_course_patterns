import os


class Links:

    HOST = "https://opensource-demo.orangehrmlive.com/web/index.php" if os.environ["STAGE"] == "dev" else "https://realese-opensource-demo.orangehrmlive.com/web/index.php"

    LOGIN_PAGE = f"{HOST}/auth/login"
    DASHBOARD_PAGE = f"{HOST}/dashboard/index"
    MY_INFO_PAGE = f"{HOST}/pim/viewPersonalDetails/empNumber/7"
    ADMIN_PAGE = f"{HOST}/admin/viewSystemUsers"