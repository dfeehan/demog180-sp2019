test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type':'wwpp',
      'cases': [
        {

          'code': """
          >>> (round(married_spouses_proportion_1985, 2) == 0.67) and (round(married_spouses_proportion_2004, 2) == 0.58)
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
