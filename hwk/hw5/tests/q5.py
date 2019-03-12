test = {
  'name': 'q5',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> get_average_degree_of_neighbors(one_network, 3)
          9.25
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> get_average_degree_of_neighbors(one_network, 10)
          7.25
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
