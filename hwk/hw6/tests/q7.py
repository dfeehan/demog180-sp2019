test = {
  'name': 'q7',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(gender_degree.where("gender","F").column('degree mean')[0],3)
          197.286
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(gender_degree.where("gender","M").column('degree mean')[0],3)
          180.679
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
