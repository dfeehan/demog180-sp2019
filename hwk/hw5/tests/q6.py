test = {
  'name': 'q6',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> np.round(np.mean(nbr_avg_degrees['avg_friends_degree']), 2)
          7.71
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(nbr_avg_degrees.where(nbr_avg_degrees['id'] == 6)['avg_friends_degree'][0]), 2) == 5.4
          True
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
