test = {
  'name': 'q2',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> beta_sim_res.num_rows
          8000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> beta_sim_res.group('beta')
          beta | count
          0.1  | 1000
          0.2  | 1000
          0.3  | 1000
          0.4  | 1000
          0.5  | 1000
          0.6  | 1000
          0.7  | 1000
          0.8  | 1000
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
