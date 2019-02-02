test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
    'type':'wwpp',
      'cases': [
        {
          'code': """
          >>> (gss_1985_long_raw.num_rows == 7655) and (gss_2004_long_raw.num_rows == 7130)
          True
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
