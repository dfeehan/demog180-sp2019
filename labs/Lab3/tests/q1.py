test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'type':'wwpp',
      'cases': [
        {
          
          'code': """
          >>> len(test.nodes()) == 8 & len(test.edges()) == 8
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