from Tests import TestCaseBase, check_status_code


class GetUrlTest(TestCaseBase):

    def setUp(self):
        super(GetUrlTest, self).setUp()
        self.short_url = self.save_url_request()

    @check_status_code(302)
    def test_success_get_url(self):
        rv = self.get_url_request('b')
        self.assertEqual(rv.handlers['location'], 'http://blog.jaehoon.kim')
        return rv

    @check_status_code(204)
    def test_wrong_url(self):
        return self.get_url_request('Pizza')
