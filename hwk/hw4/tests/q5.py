test = {
  'name': 'q5',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> add_health_clustering.num_rows
          84
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(float(np.corrcoef(add_health_clustering.column('num_nodes'), add_health_clustering.column('avg_clustering_coef'))[0,1]), 2)
          -0.66
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
