from api.tests.api_test_base import APITest
from ecwsp.grades.models import Grade

import sys

class GradeAPIPermissionsTest(APITest):
    """
    test the implementation of permissions on our grades api
    """

    def test_generic_get_request_permissions(self):
        """
        test a generic get request with both auth'd and non-auth'd users
        """

        # try it with a no authentication
        response = self.client.get('/api/grades/')
        self.assertEqual(response.status_code, 403)

        # try it with teacher authentication
        self.client.force_authenticate(user = self.data.teacher1)
        response = self.client.get('/api/grades/')
        self.assertEqual(response.status_code, 200)

        # try it with a student (who clearly has no authoritay)
        self.client.force_authenticate(user = self.data.student)
        response = self.client.get('/api/grades/')
        self.assertEqual(response.status_code, 403)

    def test_specific_get_request_permissions(self):
        """
        test a specific get request (/api/grades/:id) for permissions
        """

        # try it with a no authentication
        response = self.client.get('/api/grades/1/')
        self.assertEqual(response.status_code, 403)

        # try it with teacher authentication
        self.client.force_authenticate(user = self.data.teacher1)
        response = self.client.get('/api/grades/1/')
        self.assertEqual(response.status_code, 200)

        # try it with a student (who clearly has no authoritay)
        self.client.force_authenticate(user = self.data.student)
        response = self.client.get('/api/grades/1/')
        self.assertEqual(response.status_code, 403)

    def test_post_request_permissions(self):
        """
        test permissions on post request attempts
        """
        data = {'student_id': 1, 'course_section_id': 1, 'marking_period_id': 1, 'grade':100}

        # try it with a no authentication
        response = self.client.post('/api/grades/', data=data)
        self.assertEqual(response.status_code, 403)

        # try it with teacher authentication
        self.client.force_authenticate(user = self.data.teacher1)
        response = self.client.post('/api/grades/', data=data)
        self.assertEqual(response.status_code, 201)

        # try it with a student (who clearly has no authoritay)
        self.client.force_authenticate(user = self.data.student)
        response = self.client.post('/api/grades/', data=data)
        self.assertEqual(response.status_code, 403)






