test = {
  'name': 'q8',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> round(np.mean(add_health_sp.column('num_nodes')), 2)
          860.26
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(np.corrcoef(add_health_sp.column('avg_shortest_path'),add_health_sp.column('avg_degree'))[0,1],2)
          -0.65
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
