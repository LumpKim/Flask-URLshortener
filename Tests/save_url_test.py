from Tests import TestCaseBase, check_status_code


class SaveUrlTest(TestCaseBase):

    @check_status_code(201)
    def test_success_save_url(self):
        rv = self.save_url_request()
        self.assertEqual(rv.json['url'], 'http://lovalhost/b')
        return rv

    @check_status_code(201)
    def test_exist_url(self):
        rv = self.save_url_request()
        url = rv.json['output_url']
        self.assertEqual(rv.status_code, 201)

        rv2 = self.save_url_request()
        self.assertEqual(rv.json['output_url'], url)

        return rv2
