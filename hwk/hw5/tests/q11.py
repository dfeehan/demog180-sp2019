test = {
  'name': 'q11',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> str(round(float(frac_degree_lt_neighbors(add_health_networks[3])), 4))
          '0.7046'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> str(round(float(frac_degree_lt_neighbors(add_health_networks[30])), 4))
          '0.6818'
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
