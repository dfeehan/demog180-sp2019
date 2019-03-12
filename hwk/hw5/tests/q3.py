test = {
  'name': 'q3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(float(np.mean(degree_data['degree'])),2)
          6.38
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(np.sum(degree_data['degree']))) == 440
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
