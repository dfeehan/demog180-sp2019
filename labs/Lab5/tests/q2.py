test = {
  'name': 'q2',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> beta_sim_res.num_rows
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> beta_sim_res.group('beta')
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
