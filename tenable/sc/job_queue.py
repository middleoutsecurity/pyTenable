'''
job_queue
============

The following methods allow for interaction into the Tenable.sc
:sc-api:`Job Queue <jobQueue>` API.

Methods available on ``sc.jobs``:

.. rst-class:: hide-signature
.. autoclass:: JobQueueAPI

    .. automethod:: kill
    .. automethod:: details
    .. automethod:: list
'''
from .base import SCEndpoint

class JobQueueAPI(SCEndpoint):
  def list(self, fields=None):
      '''
      Retrieves the list of Jobs across the application and all Organizations.

      :sc-api:`job: list <Job.htm#JobRESTReference-/job>`

      Args:
          fields (list, optional):
              A list of attributes to return for each query.

      Returns:
          :obj:`list`:
              List of jobs definitions.

      Examples:
          Retrieve all of all of the jobs in the queue:

          >>> jobs = sc.jobs.list()
      '''

      params = dict()
      if fields:
          params['fields'] = ','.join([self._check('field', f, str)
                                        for f in fields])

      return self._api.get('job', params=params).json()['response']

  def details(self, job_id, fields=None):
      '''
      Retrieves the details for the specified job.
      :sc-api:`SC Job Details <Job.htm#JobRESTReference-/job/{id}>`
      Args:
          job_id (int): The numeric id of the job.
          fields (list, optional):
              The list of fields that are desired to be returned. For details
              on what fields are available, please refer to the details on
              the request within the job details API doc.
      Returns:
          :obj:`dict`:
              The job resource record.
      Examples:
          >>> job = sc.jobs.details(1)
      '''

      params = dict()
      if fields:
          params['fields'] = ','.join([self._check('field', f, str)
                                        for f in fields])

      return self._api.get('job/{}'.format(
             self._check('job_id', job_id, int)), params=params).json()['response']

  def kill(self, job_id):
      '''
        Kills the Job associated with {job_id}, depending on access.

        :sc-api:`job: kill <Job.htm#JobRESTReference-/job/{id}/kill>`

        Args:
            id (int): The numeric identifier for the job to kill.

        Returns:
            :obj:`str`:
                An empty response.

        Examples:
            >>> sc.jobs.kill(1)
      '''
      return self._api.post('job/{}/kill'.format(
              self._check('job_id', job_id, int))).json()['response']