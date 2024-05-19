from pages import AdminDashboardPage, CreatePostPage, LoginPage


class TestCreatePostPage:
    """Test create post page."""

    def test_successful_create_post(self, driver):
        """Test successful create post after login."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.fill_form_fields()
        login_page.press_enter_button()

        create_post_page = CreatePostPage(driver)
        create_post_page.open()
        create_post_page.fill_post_fields()
        create_post_page.click_create_button()

        post_creation_time = create_post_page.get_post_creation_time

        assert (
            create_post_page.get_notification_message
            == "Post was successfully created!"
        )
        admin_dashboard_page = AdminDashboardPage(driver)
        admin_dashboard_page.open()
        last_post_data = admin_dashboard_page.get_last_post_data
        assert last_post_data[1] == create_post_page.TEST_DATA["Author"]
        assert last_post_data[2] == create_post_page.TEST_DATA["Title"]
        assert last_post_data[3] == post_creation_time

    def test_post_validation_messages(self, driver):
        """Test showing validation messages under required fields."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.fill_form_fields()
        login_page.press_enter_button()

        create_post_page = CreatePostPage(driver)
        create_post_page.open()
        create_post_page.click_create_button()

        validation_messages_count = (
            create_post_page.get_validation_messages_count
        )
        assert (
            validation_messages_count == create_post_page.REQUIRED_FIELDS_COUNT
        )
