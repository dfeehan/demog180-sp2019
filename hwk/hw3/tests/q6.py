test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
    'type':'wwpp',
      'cases': [
        {
          'code': """
          >>> list(map(lambda x:round(x,2),add_health_df['clustering_coeff'][:5].tolist()))==[0.47, 0.33, 0.43, 0.22, 0.29]
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
